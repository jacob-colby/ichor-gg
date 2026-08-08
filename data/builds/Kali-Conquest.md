---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.37
  aspect_win_rate: 0.53
  slot_order:
  - name: Tyrfing
    pick_rate: 0.34
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.58
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.45
  - name: Odysseus' Bow
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Hastened Fatalis
      pick_rate: 0.14
      win_rate: 0.53
    - name: Book of Thoth
      pick_rate: 0.07
      win_rate: 0.59
  - name: Hastened Fatalis
    pick_rate: 0.21
    win_rate: 0.54
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.13
      win_rate: 0.53
    - name: Polynomicon
      pick_rate: 0.11
      win_rate: 0.49
  - name: Silverbranch Bow
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.4
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.48
  - name: Riptalon
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.45
    - name: Qin's Blade
      pick_rate: 0.06
      win_rate: 0.47
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.7
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.62
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.57
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.59
  - name: Death's Embrace
    pick_rate: 0.15
    win_rate: 0.55
  - name: Hunter's Cowl
    pick_rate: 0.15
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-08-08'
  god_win_rate: 0.524822695035461
  god_matches_won: 296
  god_matches_played: 564
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Tyrfing
  - Death Metal
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Silverbranch Bow, The Crusher, Jotunn''s Revenge, Riptalon, Gluttonous
    Grimoire, Death Metal, Berserker''s Shield, Lernaean Bow, Damaru, Spear of Desolation,
    Hydra''s Lament, Golden Blade, Soul Gem, Tekko-Kagi, Runeforged Hammer, Dominance,
    Bragi''s Harp, Genji''s Guard, The Reaper, Spear of the Magus, Bracer of The Abyss,
    Heartseeker, The Cosmic Horror, Demon Blade, Pharaoh''s Curse, Breastplate of
    Valor, Avenging Blade, Amanita Charm, Oni Hunter''s Garb, Titan''s Bane, Obsidian
    Shard, Yogi''s Necklace, Kinetic Cuirass, Shield Splitter, Shogun''s Ofuda, Pendulum
    Blade, Musashi''s Dual Swords, Arondight, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.52
      efficiency: 0.47
      win: 0.55
      pick: 0.34
      fit: 0.59
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.58
      pick: 0.06
      fit: 0.45
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.62
      pick: 0.14
      fit: 0.45
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
    this god: Amanita Charm, Riptalon, Berserker''s Shield, Soul Gem, Gluttonous Grimoire,
    Shield of the Phoenix, Kinetic Cuirass, The Crusher, Rod of Asclepius, Eye of
    Providence, Jotunn''s Revenge, Genji''s Guard, The Reaper, Runeforged Hammer,
    Oni Hunter''s Garb, Pharaoh''s Curse, Golden Blade, Chandra''s Grace, Death Metal,
    Blood-Bound Book, Lernaean Bow, Hydra''s Lament, Bancroft''s Talon, Shifter''s
    Shield, Breastplate of Valor, Yogi''s Necklace, Damaru, Phoenix Feather, Spectral
    Armor, Shogun''s Ofuda, Freya''s Tears, Eye of the Storm, Shield Splitter, Lifebinder,
    Erosion, Avenging Blade, Draconic Scale, Leviathan''s Hide, Spear of the Magus,
    Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.06
      fit: 0.57
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.62
      pick: 0.14
      fit: 0.27
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
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
  - Tyrfing
  - Spear of Desolation
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Spear of Desolation
  - Tyrfing
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
    for this god: Silverbranch Bow, The Crusher, Jotunn''s Revenge, Riptalon, Gluttonous
    Grimoire, Spear of Desolation, Soul Gem, Berserker''s Shield, Spear of the Magus,
    Tekko-Kagi, The Reaper, Avenging Blade, The Cosmic Horror, Death Metal, Lernaean
    Bow, Heartseeker, Hydra''s Lament, Damaru, Genji''s Guard, Runeforged Hammer,
    Obsidian Shard, Golden Blade, Titan''s Bane, Dominance, Bragi''s Harp, Pendulum
    Blade, Dreamer''s Idol, Screeching Gargoyle, Avatar''s Parashu, The World Stone,
    Doom Orb, Breastplate of Valor, Toxic Blade, Bracer of The Abyss, Amanita Charm,
    Pharaoh''s Curse, Oni Hunter''s Garb, Stone of Binding, Yogi''s Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.61
    Tyrfing:
      total: 0.5
      efficiency: 0.47
      win: 0.55
      pick: 0.34
      fit: 0.48
    Spear of Desolation:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.15
      fit: 0.47
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.06
      fit: 0.57
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.62
      pick: 0.14
      fit: 0.57
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
  - Berserker's Shield
  - Tyrfing
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Gluttonous Grimoire
  - The Crusher
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
    this god: Silverbranch Bow, Riptalon, Berserker''s Shield, Gluttonous Grimoire,
    The Crusher, Golden Blade, Jotunn''s Revenge, Lernaean Bow, Soul Gem, Spear of
    Desolation, Death Metal, Genji''s Guard, Hydra''s Lament, Damaru, Dominance, Runeforged
    Hammer, Bracer of The Abyss, The Reaper, Pharaoh''s Curse, Bragi''s Harp, Tekko-Kagi,
    Spear of the Magus, Breastplate of Valor, Toxic Blade, Amanita Charm, The Cosmic
    Horror, Oni Hunter''s Garb, Nimble Ring, Yogi''s Necklace, Kinetic Cuirass, Blood-Bound
    Book, Shogun''s Ofuda, Bancroft''s Talon, Heartseeker, Eye of Providence, Eros''
    Bow, Avenging Blade, Demon Blade, Obsidian Shard.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.26
    Tyrfing:
      total: 0.53
      efficiency: 0.47
      win: 0.55
      pick: 0.34
      fit: 0.67
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.58
      pick: 0.06
      fit: 0.65
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.62
      pick: 0.14
      fit: 0.57
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
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Silverbranch Bow
  - Soul Gem
  flex_slots:
  - Silverbranch Bow
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Spear of Desolation,
    Soul Gem, Genji''s Guard, Silverbranch Bow, Hydra''s Lament, Gluttonous Grimoire,
    Breastplate of Valor, Riptalon, The Crusher, Berserker''s Shield, Chronos'' Pendant,
    Death Metal, Freya''s Tears, Shield of the Phoenix, Lernaean Bow, Spear of the
    Magus, Gem of Focus, Damaru, Arondight, Runeforged Hammer, The Cosmic Horror,
    Bracer of The Abyss, Screeching Gargoyle, Chandra''s Grace, Pendulum Blade, Golden
    Blade, Bragi''s Harp, Amanita Charm, Oni Hunter''s Garb, Pharaoh''s Curse, Dominance,
    Yogi''s Necklace, Kinetic Cuirass, Obsidian Shard, The Reaper, Rod of Asclepius,
    Tekko-Kagi, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Spear of Desolation:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.15
      fit: 0.59
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.62
      pick: 0.14
      fit: 0.31
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
    Underrated for this god: The Crusher, Jotunn''s Revenge, Gluttonous Grimoire,
    Death Metal, Berserker''s Shield, Lernaean Bow, Damaru, Hydra''s Lament, Golden
    Blade, Soul Gem, Tekko-Kagi, Riptalon, Runeforged Hammer, Dominance, Bragi''s
    Harp, Genji''s Guard, Silverbranch Bow, The Reaper, Spear of the Magus, Bracer
    of The Abyss, Heartseeker, The Cosmic Horror, Demon Blade, Pharaoh''s Curse, Breastplate
    of Valor, Avenging Blade, Amanita Charm, Spear of Desolation, Oni Hunter''s Garb,
    Titan''s Bane, Obsidian Shard, Yogi''s Necklace, Kinetic Cuirass, Shield Splitter,
    Shogun''s Ofuda, Pendulum Blade, Musashi''s Dual Swords, Arondight, Eye of the
    Storm.'
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
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
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
      fit: 0.55
  starter: *id001
---
