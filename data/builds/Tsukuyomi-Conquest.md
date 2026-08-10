---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.24
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.45
    win_rate: 0.56
    alternates:
    - name: Transcendence
      pick_rate: 0.21
      win_rate: 0.57
    - name: Hydra's Lament
      pick_rate: 0.11
      win_rate: 0.54
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.53
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.6
  - name: Hydra's Lament
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.52
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.65
  - name: Heartseeker
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.11
      win_rate: 0.58
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.66
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.64
    - name: Lucerne Hammer
      pick_rate: 0.05
      win_rate: 0.64
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.68
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.37
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.24
    win_rate: 0.51
  - name: Archmage's Gem
    pick_rate: 0.11
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-10'
  god_win_rate: 0.5575065847234416
  god_matches_won: 635
  god_matches_played: 1139
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - The Crusher
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, The Crusher, Gluttonous Grimoire, Death
    Metal, Berserker''s Shield, Lernaean Bow, Damaru, Golden Blade, Soul Gem, Tekko-Kagi,
    Riptalon, Runeforged Hammer, Dominance, Bragi''s Harp, Genji''s Guard, Silverbranch
    Bow, Tyrfing, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror, Pharaoh''s
    Curse, Demon Blade, Breastplate of Valor, Avenging Blade, Amanita Charm, Spear
    of Desolation, Oni Hunter''s Garb, Obsidian Shard, Yogi''s Necklace, Kinetic Cuirass,
    Shield Splitter, Shogun''s Ofuda, Pendulum Blade, Musashi''s Dual Swords, Arondight,
    Eye of the Storm.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.49
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - The Crusher
  flex_slots:
  - Death Metal
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Reaper, Hydra''s Lament, Gluttonous Grimoire, Soul Gem, The Crusher,
    Death Metal, Genji''s Guard, Berserker''s Shield, Spear of the Magus, Spear of
    Desolation, The Cosmic Horror, Lernaean Bow, Riptalon, Breastplate of Valor, Damaru,
    Runeforged Hammer, Silverbranch Bow, Obsidian Shard, Bragi''s Harp, Bracer of
    The Abyss, Chronos'' Pendant, Tekko-Kagi, Golden Blade, Dominance, Dreamer''s
    Idol, Rod of Asclepius, Amanita Charm, Pendulum Blade, The World Stone, Doom Orb,
    Freya''s Tears, Oni Hunter''s Garb, Tyrfing, Blood-Bound Book, Helm of Radiance,
    Yogi''s Necklace, Bancroft''s Talon, Gem of Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.16
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.56
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.42
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.54
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.4
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, Berserker''s Shield, Hydra''s Lament, Soul
    Gem, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Rod of Asclepius, Riptalon, Eye of Providence, Genji''s Guard, Oni Hunter''s Garb,
    Runeforged Hammer, Pharaoh''s Curse, Golden Blade, Chandra''s Grace, Blood-Bound
    Book, Death Metal, Lernaean Bow, Bancroft''s Talon, Shifter''s Shield, Breastplate
    of Valor, Yogi''s Necklace, Damaru, Phoenix Feather, Spectral Armor, Shogun''s
    Ofuda, Lifebinder, Freya''s Tears, Eye of the Storm, Shield Splitter, Erosion,
    Avenging Blade, Draconic Scale, Spear of the Magus, Leviathan''s Hide, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.27
    The Reaper:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Titan's Bane
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, The Crusher, Gluttonous Grimoire, Hydra''s Lament, Soul
    Gem, Riptalon, Berserker''s Shield, Spear of the Magus, Silverbranch Bow, Tekko-Kagi,
    The Cosmic Horror, Avenging Blade, Death Metal, Lernaean Bow, Damaru, Genji''s
    Guard, Spear of Desolation, Obsidian Shard, Runeforged Hammer, Golden Blade, Dominance,
    Bragi''s Harp, Pendulum Blade, Tyrfing, Dreamer''s Idol, Screeching Gargoyle,
    The World Stone, Doom Orb, Avatar''s Parashu, Breastplate of Valor, Toxic Blade,
    Bracer of The Abyss, Amanita Charm, Pharaoh''s Curse, Oni Hunter''s Garb, Stone
    of Binding, Yogi''s Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.6
    Hydra's Lament:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.32
    The Reaper:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.57
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.51
      efficiency: 0.46
      win: 0.53
      pick: 0.21
      fit: 0.67
    Titan's Bane:
      total: 0.51
      efficiency: 0.46
      win: 0.56
      pick: 0.16
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Riptalon
  flex_slots:
  - Berserker's Shield
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Hydra''s Lament, Riptalon, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Golden Blade, Silverbranch Bow, Lernaean Bow, Soul Gem, Tyrfing,
    Death Metal, Genji''s Guard, Damaru, Dominance, Runeforged Hammer, Bracer of The
    Abyss, Bragi''s Harp, Pharaoh''s Curse, Tekko-Kagi, Spear of the Magus, Breastplate
    of Valor, Toxic Blade, Amanita Charm, The Cosmic Horror, Oni Hunter''s Garb, Nimble
    Ring, Yogi''s Necklace, Kinetic Cuirass, Blood-Bound Book, Shogun''s Ofuda, Bancroft''s
    Talon, Eye of Providence, Eros'' Bow, Spear of Desolation, Obsidian Shard, Avenging
    Blade, Demon Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.3
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.27
    The Reaper:
      total: 0.54
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Soul Gem, Genji''s
    Guard, The Reaper, Gluttonous Grimoire, Breastplate of Valor, The Crusher, Berserker''s
    Shield, Spear of Desolation, Chronos'' Pendant, Death Metal, Freya''s Tears, Shield
    of the Phoenix, Lernaean Bow, Spear of the Magus, Gem of Focus, Damaru, Arondight,
    Riptalon, Runeforged Hammer, The Cosmic Horror, Bracer of The Abyss, Screeching
    Gargoyle, Chandra''s Grace, Silverbranch Bow, Pendulum Blade, Golden Blade, Bragi''s
    Harp, Amanita Charm, Oni Hunter''s Garb, Pharaoh''s Curse, Dominance, Yogi''s
    Necklace, Kinetic Cuirass, Obsidian Shard, Rod of Asclepius, Tekko-Kagi, Tyrfing,
    Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.59
    Hydra's Lament:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.55
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - Spear of the Magus
  - The Crusher
  flex_slots:
  - Death Metal
  - Spear of the Magus
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
    + win/pick). Underrated for this god: Hydra''s Lament, The Reaper, Gluttonous
    Grimoire, Soul Gem, The Crusher, Death Metal, Spear of the Magus, Berserker''s
    Shield, Genji''s Guard, Spear of Desolation, The Cosmic Horror, Bragi''s Harp,
    Bracer of The Abyss, Lernaean Bow, Chronos'' Pendant, Damaru, Obsidian Shard,
    Runeforged Hammer, Breastplate of Valor, Rod of Asclepius, Riptalon, Golden Blade,
    Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Silverbranch Bow, Jade
    Scepter, Dominance, Gem of Focus, Tekko-Kagi, Dreamer''s Idol, The World Stone,
    Doom Orb, Nimble Ring, Amanita Charm, Tyrfing, Oni Hunter''s Garb, Pharaoh''s
    Curse, Yogi''s Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.46
    Hydra's Lament:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.53
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.33
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - The Reaper
  - The Crusher
  flex_slots:
  - Death Metal
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: The Reaper, Hydra''s Lament, Gluttonous
    Grimoire, The Crusher, Death Metal, Soul Gem, Berserker''s Shield, Spear of the
    Magus, Lernaean Bow, Bragi''s Harp, The Cosmic Horror, Damaru, Bracer of The Abyss,
    Runeforged Hammer, Genji''s Guard, Golden Blade, Riptalon, Spear of Desolation,
    Tekko-Kagi, Obsidian Shard, Dominance, Silverbranch Bow, Tyrfing, Rod of Asclepius,
    Blood-Bound Book, Helm of Radiance, Bancroft''s Talon, Chronos'' Pendant, Breastplate
    of Valor, Dreamer''s Idol, Jade Scepter, The World Stone, Doom Orb, Nimble Ring,
    Amanita Charm, Triton''s Conch, Pharaoh''s Curse, Oni Hunter''s Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.44
    Hydra's Lament:
      total: 0.53
      efficiency: 0.61
      win: 0.58
      pick: 0.15
      fit: 0.36
    Death Metal:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Reaper:
      total: 0.55
      efficiency: 0.53
      win: 0.65
      pick: 0.1
      fit: 0.41
    The Crusher:
      total: 0.53
      efficiency: 0.65
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
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Gluttonous Grimoire, Death Metal, Berserker''s
    Shield, Lernaean Bow, Damaru, Hydra''s Lament, Golden Blade, Soul Gem, Tekko-Kagi,
    Riptalon, Runeforged Hammer, Dominance, Bragi''s Harp, Genji''s Guard, Silverbranch
    Bow, Tyrfing, The Reaper, Spear of the Magus, Bracer of The Abyss, The Cosmic
    Horror, Pharaoh''s Curse, Demon Blade, Breastplate of Valor, Avenging Blade, Amanita
    Charm, Spear of Desolation, Oni Hunter''s Garb, Obsidian Shard, Yogi''s Necklace,
    Kinetic Cuirass, Shield Splitter, Shogun''s Ofuda, Pendulum Blade, Musashi''s
    Dual Swords, Arondight, Eye of the Storm.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.45
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
