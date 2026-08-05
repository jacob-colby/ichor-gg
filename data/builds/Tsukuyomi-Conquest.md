---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.0
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.39
    win_rate: 0.54
    alternates:
    - name: Transcendence
      pick_rate: 0.23
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.53
  - name: Transcendence
    pick_rate: 0.24
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.19
      win_rate: 0.56
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.54
  - name: Hydra's Lament
    pick_rate: 0.15
    win_rate: 0.51
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.5
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.68
  - name: Heartseeker
    pick_rate: 0.2
    win_rate: 0.46
    alternates:
    - name: Titan's Bane
      pick_rate: 0.13
      win_rate: 0.47
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.56
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.2
      win_rate: 0.67
    - name: Void Shard
      pick_rate: 0.06
      win_rate: 0.5
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 0.3
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.77
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-01'
  god_win_rate: 0.55078125
  god_matches_won: 141
  god_matches_played: 256
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Damaru
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Damaru
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Lernaean Bow, Hydra''s Lament, Damaru, Berserker''s Shield,
    Runeforged Hammer, Golden Blade, Tekko-Kagi, Riptalon, The Reaper, Tyrfing, Avenging
    Blade, Demon Blade, Genji''s Guard, Avatar''s Parashu, Pharaoh''s Curse, Arondight,
    Eros'' Bow, Oni Hunter''s Garb, Yogi''s Necklace, Shield Splitter, Pendulum Blade,
    Breastplate of Valor, Eye of the Storm, Musashi''s Dual Swords.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.41
    Damaru:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
    Titan's Bane:
      total: 0.53
      efficiency: 0.51
      win: 0.6
      pick: 0.18
      fit: 0.47
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Lernaean Bow
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, Lernaean Bow, Runeforged Hammer, Berserker''s
    Shield, Genji''s Guard, Damaru, Riptalon, The Reaper, Golden Blade, Tekko-Kagi,
    Breastplate of Valor, Avenging Blade, Arondight, Avatar''s Parashu, Pendulum Blade,
    Pharaoh''s Curse, Oni Hunter''s Garb, Tyrfing, Yogi''s Necklace, Kinetic Cuirass,
    Shield of the Phoenix, Amanita Charm, Chandra''s Grace, Spectral Armor.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.56
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.26
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.5
    Titan's Bane:
      total: 0.52
      efficiency: 0.51
      win: 0.6
      pick: 0.18
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Runeforged
    Hammer, Kinetic Cuirass, The Crusher, Riptalon, Hydra''s Lament, The Reaper, Pharaoh''s
    Curse, Oni Hunter''s Garb, Golden Blade, Eye of Providence, Lernaean Bow, Chandra''s
    Grace, Genji''s Guard, Avenging Blade, Spectral Armor, Damaru, Eye of the Storm,
    Yogi''s Necklace, Shogun''s Ofuda, Phoenix Feather, Shield Splitter, Shifter''s
    Shield, Bloodforge, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.31
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.51
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Hydra''s Lament, Riptalon, Lernaean
    Bow, The Reaper, Tekko-Kagi, Berserker''s Shield, Runeforged Hammer, Damaru, Avatar''s
    Parashu, Golden Blade, Genji''s Guard, Pendulum Blade, Tyrfing, Pharaoh''s Curse,
    Oni Hunter''s Garb, Yogi''s Necklace, Demon Blade, Arondight, Oath-Sworn Spear,
    Breastplate of Valor, Kinetic Cuirass, Screeching Gargoyle, Eros'' Bow.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.6
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.64
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.33
    Riptalon:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.57
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.7
    Titan's Bane:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.18
      fit: 0.6
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Golden Blade, Lernaean Bow, The Crusher, Berserker''s Shield,
    Hydra''s Lament, Tyrfing, Runeforged Hammer, Damaru, The Reaper, Pharaoh''s Curse,
    Genji''s Guard, Tekko-Kagi, Avenging Blade, Eros'' Bow, Oni Hunter''s Garb, Yogi''s
    Necklace, Demon Blade, Shogun''s Ofuda, Kinetic Cuirass, Breastplate of Valor,
    Amanita Charm, Avatar''s Parashu, Barbed Carver, Spectral Armor, Arondight.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.59
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.32
    Riptalon:
      total: 0.54
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Genji''s Guard, The
    Crusher, Breastplate of Valor, Berserker''s Shield, Lernaean Bow, Runeforged Hammer,
    Arondight, Shield of the Phoenix, Damaru, Chandra''s Grace, Golden Blade, Freya''s
    Tears, Riptalon, Pendulum Blade, Avenging Blade, Pharaoh''s Curse, Oni Hunter''s
    Garb, Yogi''s Necklace, The Reaper, Kinetic Cuirass, Screeching Gargoyle, Tekko-Kagi,
    Tyrfing, Amanita Charm, Eros'' Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.34
    Berserker's Shield:
      total: 0.51
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.17
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.59
    Hydra's Lament:
      total: 0.56
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Death Metal
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Soul Gem, Hydra''s
    Lament, The Crusher, Death Metal, Lernaean Bow, Bragi''s Harp, Runeforged Hammer,
    Berserker''s Shield, Ethereal Staff, Spear of the Magus, Bracer of The Abyss,
    Genji''s Guard, Damaru, Golden Blade, The Cosmic Horror, Spear of Desolation,
    Chronos'' Pendant, Wish-Granting Pearl, Riptalon, Jade Scepter, Avenging Blade,
    Bancroft''s Talon, Rod of Asclepius, Blood-Bound Book, The Reaper, Nimble Ring,
    Triton''s Conch, Breastplate of Valor, Obsidian Shard, Tekko-Kagi, Arondight,
    Pharaoh''s Curse, Oni Hunter''s Garb, Gem of Focus, Dreamer''s Idol, Helm of Radiance.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.46
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.39
    Death Metal:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Hydra's Lament
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher,
    Death Metal, Hydra''s Lament, Lernaean Bow, Soul Gem, Bragi''s Harp, Runeforged
    Hammer, Berserker''s Shield, Damaru, Golden Blade, Ethereal Staff, Spear of the
    Magus, Bracer of The Abyss, The Reaper, Avenging Blade, Riptalon, The Cosmic Horror,
    Tekko-Kagi, Genji''s Guard, Triton''s Conch, Wish-Granting Pearl, Tyrfing, Jade
    Scepter, Nimble Ring, Avatar''s Parashu, Bancroft''s Talon, Rod of Asclepius,
    Blood-Bound Book, Obsidian Shard, Pharaoh''s Curse, Spear of Desolation, Oni Hunter''s
    Garb, Dreamer''s Idol, Chronos'' Pendant, Arondight, Yogi''s Necklace.'
  slot_scores:
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.44
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.36
    Death Metal:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Damaru
  - The Crusher
  flex_slots:
  - Damaru
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Lernaean Bow, Hydra''s Lament, Damaru, Berserker''s
    Shield, Runeforged Hammer, Golden Blade, Tekko-Kagi, Riptalon, The Reaper, Tyrfing,
    Avenging Blade, Demon Blade, Genji''s Guard, Avatar''s Parashu, Pharaoh''s Curse,
    Arondight, Eros'' Bow, Oni Hunter''s Garb, Yogi''s Necklace, Shield Splitter,
    Pendulum Blade, Breastplate of Valor, Eye of the Storm, Musashi''s Dual Swords.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Berserker's Shield:
      total: 0.52
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.27
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.54
      pick: 0.39
      fit: 0.52
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.51
      pick: 0.15
      fit: 0.41
    Damaru:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.57
  starter: *id001
---
