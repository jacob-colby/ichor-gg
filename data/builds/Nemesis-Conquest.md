---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.36
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.3
      win_rate: 0.6
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.35
  - name: Hydra's Lament
    pick_rate: 0.24
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.58
    - name: Dagger of Frenzy
      pick_rate: 0.08
      win_rate: 0.5
  - name: The Reaper
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.6
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.15
    win_rate: 0.51
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.55
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.6
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.65
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Blinking Abyss
      pick_rate: 0.08
      win_rate: 0.71
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.47
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.3
    win_rate: 0.58
  - name: Bumba's Cudgel
    pick_rate: 0.24
    win_rate: 0.46
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.65
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-10'
  god_win_rate: 0.5274542429284526
  god_matches_won: 317
  god_matches_played: 601
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
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - The Reaper
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, The Crusher, Gluttonous Grimoire, Death Metal, Berserker''s
    Shield, Lernaean Bow, Damaru, Golden Blade, Soul Gem, Tekko-Kagi, Riptalon, Runeforged
    Hammer, Dominance, Bragi''s Harp, Genji''s Guard, Silverbranch Bow, Titan''s Bane,
    Tyrfing, Heartseeker, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror,
    Demon Blade, Pharaoh''s Curse, Breastplate of Valor, Amanita Charm, Spear of Desolation,
    Oni Hunter''s Garb, Obsidian Shard, Yogi''s Necklace, Kinetic Cuirass, Shield
    Splitter, Shogun''s Ofuda, Pendulum Blade, Musashi''s Dual Swords, Arondight,
    Eye of the Storm, Avenging Blade.'
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
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.49
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Reaper:
      total: 0.54
      efficiency: 0.53
      win: 0.63
      pick: 0.11
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
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    this god: The Reaper, Amanita Charm, Berserker''s Shield, Shifter''s Shield, Soul
    Gem, Gluttonous Grimoire, Shield of the Phoenix, Kinetic Cuirass, The Crusher,
    Rod of Asclepius, Riptalon, Eye of Providence, Genji''s Guard, Runeforged Hammer,
    Oni Hunter''s Garb, Pharaoh''s Curse, Golden Blade, Chandra''s Grace, Death Metal,
    Blood-Bound Book, Lernaean Bow, Bancroft''s Talon, Breastplate of Valor, Yogi''s
    Necklace, Damaru, Phoenix Feather, Spectral Armor, Shogun''s Ofuda, Freya''s Tears,
    Eye of the Storm, Lifebinder, Shield Splitter, Erosion, Draconic Scale, Spear
    of the Magus, Leviathan''s Hide, Dominance, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Reaper:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.11
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.09
      fit: 0.39
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
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Spear of the Magus
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Spear of the Magus
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, The Crusher, Gluttonous Grimoire, Soul Gem, Riptalon,
    Berserker''s Shield, Spear of the Magus, Tekko-Kagi, Silverbranch Bow, Titan''s
    Bane, Heartseeker, The Cosmic Horror, Death Metal, Lernaean Bow, Damaru, Genji''s
    Guard, Spear of Desolation, Runeforged Hammer, Obsidian Shard, Golden Blade, Dominance,
    Bragi''s Harp, Pendulum Blade, Tyrfing, Dreamer''s Idol, Screeching Gargoyle,
    The World Stone, Avatar''s Parashu, Doom Orb, Breastplate of Valor, Toxic Blade,
    Bracer of The Abyss, Amanita Charm, Pharaoh''s Curse, Oni Hunter''s Garb, Stone
    of Binding, Yogi''s Necklace, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.61
    The Reaper:
      total: 0.56
      efficiency: 0.53
      win: 0.63
      pick: 0.11
      fit: 0.57
    Spear of the Magus:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.46
      win: 0.5
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Reaper
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Riptalon, Berserker''s Shield, Gluttonous Grimoire, The
    Crusher, Golden Blade, Silverbranch Bow, Lernaean Bow, Tyrfing, Soul Gem, Death
    Metal, Genji''s Guard, Damaru, Dominance, Runeforged Hammer, Bracer of The Abyss,
    Bragi''s Harp, Pharaoh''s Curse, Tekko-Kagi, Spear of the Magus, Breastplate of
    Valor, Toxic Blade, Amanita Charm, The Cosmic Horror, Heartseeker, Oni Hunter''s
    Garb, Nimble Ring, Yogi''s Necklace, Kinetic Cuirass, Blood-Bound Book, Shogun''s
    Ofuda, Bancroft''s Talon, Eye of Providence, Eros'' Bow, Spear of Desolation,
    Obsidian Shard, Demon Blade, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.57
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.31
    The Reaper:
      total: 0.53
      efficiency: 0.53
      win: 0.63
      pick: 0.11
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, The Reaper,
    Gluttonous Grimoire, Breastplate of Valor, The Crusher, Berserker''s Shield, Spear
    of Desolation, Chronos'' Pendant, Death Metal, Freya''s Tears, Shield of the Phoenix,
    Lernaean Bow, Spear of the Magus, Gem of Focus, Damaru, Arondight, Riptalon, Runeforged
    Hammer, The Cosmic Horror, Bracer of The Abyss, Screeching Gargoyle, Chandra''s
    Grace, Silverbranch Bow, Pendulum Blade, Golden Blade, Bragi''s Harp, Amanita
    Charm, Oni Hunter''s Garb, Pharaoh''s Curse, Dominance, Yogi''s Necklace, Kinetic
    Cuirass, Obsidian Shard, Rod of Asclepius, Tekko-Kagi, Tyrfing, Blood-Bound Book.'
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
      total: 0.57
      efficiency: 0.65
      win: 0.53
      pick: 0.36
      fit: 0.59
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.45
      pick: 0.24
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
    Shield, Lernaean Bow, Damaru, Golden Blade, Soul Gem, Tekko-Kagi, Riptalon, Runeforged
    Hammer, Dominance, Bragi''s Harp, Genji''s Guard, Silverbranch Bow, Tyrfing, The
    Reaper, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror, Heartseeker,
    Demon Blade, Pharaoh''s Curse, Breastplate of Valor, Avenging Blade, Amanita Charm,
    Spear of Desolation, Oni Hunter''s Garb, Titan''s Bane, Obsidian Shard, Yogi''s
    Necklace, Kinetic Cuirass, Shield Splitter, Shogun''s Ofuda, Pendulum Blade, Musashi''s
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
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.36
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
      fit: 0.36
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
---
