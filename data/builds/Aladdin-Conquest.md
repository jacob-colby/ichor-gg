---
type: smite-build
god: Aladdin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Genie's Lamp
    pick_rate: 0.75
    win_rate: 0.48
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.63
    - name: Jotunn's Revenge
      pick_rate: 0.04
      win_rate: 0.63
  - name: Spear of Desolation
    pick_rate: 0.38
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.2
      win_rate: 0.52
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.52
  - name: Book of Thoth
    pick_rate: 0.19
    win_rate: 0.49
    alternates:
    - name: Transcendence
      pick_rate: 0.13
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.43
  - name: Polynomicon
    pick_rate: 0.25
    win_rate: 0.48
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.16
      win_rate: 0.52
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.6
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.15
      win_rate: 0.58
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.48
  - name: Obsidian Shard
    pick_rate: 0.19
    win_rate: 0.65
    alternates:
    - name: Void Shard
      pick_rate: 0.07
      win_rate: 0.35
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.47
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.22
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.09
    win_rate: 0.68
  source_url: https://smitebrain.com/gods/aladdin/
  last_verified: '2026-08-19'
  god_win_rate: 0.5196078431372549
  god_matches_won: 212
  god_matches_played: 408
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    this god: The Crusher, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, The Reaper,
    Pendulum Blade, Titan''s Bane, Genji''s Guard, Death Metal, The Cosmic Horror,
    Runeforged Hammer, Spear of the Magus, Tekko-Kagi, Damaru, Nimble Ring, Breastplate
    of Valor, Arondight, Lernaean Bow, Golden Blade, Avenging Blade, Chronos'' Pendant,
    Dominance, Freya''s Tears, Shield Splitter, Bragi''s Harp, Avatar''s Parashu,
    Riptalon, Eye of the Storm, Tyrfing, Berserker''s Shield, Silverbranch Bow, Shield
    of the Phoenix, Totem of Death, Triton''s Conch, Doom Orb, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.49
      pick: 0.3
      fit: 0.1
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.9
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.2
      fit: 0.38
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.42
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.52
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: The
    Crusher, Gluttonous Grimoire, Soul Gem, Hydra''s Lament, Nimble Ring, Death Metal,
    Genji''s Guard, The Cosmic Horror, Spear of the Magus, Breastplate of Valor, Chronos''
    Pendant, The Reaper, Runeforged Hammer, Doom Orb, Bragi''s Harp, The World Stone,
    Totem of Death, Bancroft''s Talon, Damaru, Titan''s Bane, Triton''s Conch, Dominance,
    Helm of Radiance, Ethereal Staff, Pendulum Blade, Gem of Focus, Blood-Bound Book,
    Rod of Asclepius, Lernaean Bow, Arondight, Oni Hunter''s Garb, Berserker''s Shield,
    Golden Blade, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.49
      win: 0.49
      pick: 0.3
      fit: 0.39
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.71
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.2
      fit: 0.39
    Hydra's Lament:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.57
    Obsidian Shard:
      total: 0.59
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, The Crusher, Gluttonous Grimoire, The Cosmic Horror, Spear of the
    Magus, Hydra''s Lament, Genji''s Guard, Nimble Ring, The Reaper, Death Metal,
    Pendulum Blade, Chronos'' Pendant, Breastplate of Valor, Titan''s Bane, Totem
    of Death, Doom Orb, The World Stone, Runeforged Hammer, Freya''s Tears, Tekko-Kagi,
    Gem of Focus, Dreamer''s Idol, Riptalon, Arondight, Damaru, Silverbranch Bow,
    Shield of the Phoenix, Berserker''s Shield, Bragi''s Harp, Helm of Radiance, Ethereal
    Staff, Blood-Bound Book, Rod of Asclepius, Lernaean Bow, Kinetic Cuirass, Amanita
    Charm, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.78
    Spear of Desolation:
      total: 0.55
      efficiency: 0.52
      win: 0.5
      pick: 0.52
      fit: 0.78
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.56
    Obsidian Shard:
      total: 0.6
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.66
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Gluttonous
    Grimoire, The Crusher, Berserker''s Shield, Genji''s Guard, The Reaper, Ethereal
    Staff, Chandra''s Grace, Rod of Asclepius, Yogi''s Necklace, Freya''s Tears, Oni
    Hunter''s Garb, Runeforged Hammer, Breastplate of Valor, Phoenix Feather, Erosion,
    Eye of the Storm, Shifter''s Shield, Spectral Armor, Riptalon, Hydra''s Lament,
    Eye of Providence, Shield Splitter, Draconic Scale, Nimble Ring, Blood-Bound Book,
    Pharaoh''s Curse, Golden Blade, Leviathan''s Hide, Lifebinder, Midgardian Mail,
    Avenging Blade, Bancroft''s Talon, The Cosmic Horror, Glorious Pridwen, Death
    Metal, Ancile.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.75
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.44
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Gluttonous Grimoire
  - Transcendence
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Gluttonous Grimoire, Soul Gem, The Reaper, The Cosmic
    Horror, Spear of the Magus, Titan''s Bane, Pendulum Blade, Tekko-Kagi, Hydra''s
    Lament, Riptalon, Avenging Blade, Genji''s Guard, Silverbranch Bow, Screeching
    Gargoyle, Doom Orb, The World Stone, Nimble Ring, Avatar''s Parashu, Runeforged
    Hammer, Death Metal, Dreamer''s Idol, Breastplate of Valor, Damaru, Toxic Blade,
    Lernaean Bow, Berserker''s Shield, Freya''s Tears, Arondight, Stone of Binding,
    Golden Blade, Chronos'' Pendant, Kinetic Cuirass, Void Shield, Amanita Charm,
    Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.93
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.58
      pick: 0.2
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.89
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.6
    Obsidian Shard:
      total: 0.61
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Riptalon
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Riptalon, The Crusher, Gluttonous Grimoire, Golden Blade,
    Silverbranch Bow, Soul Gem, Berserker''s Shield, Tyrfing, Genji''s Guard, Lernaean
    Bow, Hydra''s Lament, Dominance, Toxic Blade, Tekko-Kagi, The Reaper, Breastplate
    of Valor, Pharaoh''s Curse, The Cosmic Horror, Bragi''s Harp, Spear of the Magus,
    Runeforged Hammer, Bracer of The Abyss, Death Metal, Qin''s Blade, Kinetic Cuirass,
    Damaru, Amanita Charm, Freya''s Tears, Shogun''s Ofuda, Eye of Providence, Titan''s
    Bane, Oni Hunter''s Garb, Chronos'' Pendant, Blood-Bound Book, Shield of the Phoenix,
    Eros'' Bow.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.61
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.39
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.2
    Obsidian Shard:
      total: 0.55
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Genji's Guard
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
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Hydra''s
    Lament, Breastplate of Valor, The Crusher, Chronos'' Pendant, Gluttonous Grimoire,
    Freya''s Tears, Totem of Death, Shield of the Phoenix, Pendulum Blade, Gem of
    Focus, Arondight, Nimble Ring, Screeching Gargoyle, Chandra''s Grace, The Cosmic
    Horror, Spear of the Magus, Death Metal, The Reaper, Gladiator''s Shield, Runeforged
    Hammer, Berserker''s Shield, Prophetic Cloak, Titan''s Bane, Kinetic Cuirass,
    Damaru, Amanita Charm, Helm of Radiance, Riptalon, Eye of Providence, Ethereal
    Staff, Doom Orb, Oni Hunter''s Garb, Blood-Bound Book, Rod of Asclepius, Regrowth
    Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.85
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.5
      pick: 0.52
      fit: 0.85
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.45
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - The Crusher
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Transcendence
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
    Underrated for this god: The Crusher, Soul Gem, Gluttonous Grimoire, Hydra''s
    Lament, The Reaper, Pendulum Blade, Titan''s Bane, Genji''s Guard, Death Metal,
    The Cosmic Horror, Runeforged Hammer, Spear of the Magus, Tekko-Kagi, Damaru,
    Nimble Ring, Breastplate of Valor, Arondight, Lernaean Bow, Golden Blade, Avenging
    Blade, Chronos'' Pendant, Dominance, Freya''s Tears, Shield Splitter, Bragi''s
    Harp, Avatar''s Parashu, Riptalon, Eye of the Storm, Tyrfing, Berserker''s Shield,
    Silverbranch Bow, Shield of the Phoenix, Totem of Death, Triton''s Conch, Doom
    Orb, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.9
    Transcendence:
      total: 0.51
      efficiency: 0.52
      win: 0.58
      pick: 0.2
      fit: 0.38
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.42
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Obsidian Shard
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: The Crusher, Soul Gem, Gluttonous
    Grimoire, Hydra''s Lament, The Reaper, Pendulum Blade, Titan''s Bane, Genji''s
    Guard, Death Metal, The Cosmic Horror, Runeforged Hammer, Spear of the Magus,
    Tekko-Kagi, Damaru, Nimble Ring, Breastplate of Valor, Arondight, Lernaean Bow,
    Golden Blade, Avenging Blade, Chronos'' Pendant, Dominance, Freya''s Tears, Shield
    Splitter, Bragi''s Harp, Avatar''s Parashu, Riptalon, Eye of the Storm, Tyrfing,
    Berserker''s Shield, Silverbranch Bow, Shield of the Phoenix, Totem of Death,
    Triton''s Conch, Doom Orb, The World Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.64
      win: 0.52
      pick: 0.27
      fit: 0.9
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.68
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.79
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.77
      win: 0.5
      pick: 0.71
      fit: 0.42
    Obsidian Shard:
      total: 0.58
      efficiency: 0.52
      win: 0.65
      pick: 0.58
      fit: 0.52
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
  swaps:
  - added: Obsidian Shard
    removed: Transcendence
    reason: community 65% win over 78 matches (vs 52% on this god), taking the model's
      weakest slot from Transcendence
  starter: *id001
---
