---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.52
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.45
    win_rate: 0.51
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.25
      win_rate: 0.42
    - name: Avenging Blade
      pick_rate: 0.07
      win_rate: 0.38
  - name: Hydra's Lament
    pick_rate: 0.32
    win_rate: 0.43
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.46
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.58
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.5
  - name: Heartseeker
    pick_rate: 0.21
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.35
    - name: The Reaper
      pick_rate: 0.06
      win_rate: 0.46
  - name: Titan's Bane
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.45
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.62
  - name: Blinking Abyss
    pick_rate: 0.11
    win_rate: 0.58
    alternates:
    - name: Skeggox
      pick_rate: 0.07
      win_rate: 0.75
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 0.25
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.31
    win_rate: 0.57
  - name: Bumba's Cudgel
    pick_rate: 0.23
    win_rate: 0.44
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-17'
  god_win_rate: 0.4863636363636364
  god_matches_won: 107
  god_matches_played: 220
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-17'
  god_matches_analyzed: 7467
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Damaru
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Damaru
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
    this god: Rod of Tahuti, The Crusher, Nimble Ring, Gluttonous Grimoire, Death
    Metal, Berserker''s Shield, Damaru, Lernaean Bow, Soul Gem, Golden Blade, Tekko-Kagi,
    Riptalon, Tyrfing, Silverbranch Bow, Genji''s Guard, Bragi''s Harp, Runeforged
    Hammer, The Cosmic Horror, Spear of the Magus, Dominance, Transcendence, Breastplate
    of Valor, Pharaoh''s Curse, Spear of Desolation, Demon Blade, Bracer of The Abyss,
    Deathbringer, Kinetic Cuirass, Obsidian Shard, Amanita Charm, Toxic Blade, Pendulum
    Blade, Eye of Providence, Shield Splitter, Oni Hunter''s Garb, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.49
    Death Metal:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.5
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.36
    Damaru:
      total: 0.5
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Death Metal
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Nimble Ring, The Crusher, Gluttonous Grimoire, Soul Gem, Death Metal,
    Genji''s Guard, The Cosmic Horror, Berserker''s Shield, Spear of the Magus, Spear
    of Desolation, Breastplate of Valor, Damaru, Bragi''s Harp, Lernaean Bow, Transcendence,
    Golden Blade, Runeforged Hammer, Chronos'' Pendant, Obsidian Shard, Bracer of
    The Abyss, Dominance, Tyrfing, Riptalon, Tekko-Kagi, Bancroft''s Talon, Oni Hunter''s
    Garb, Helm of Radiance, Doom Orb, Silverbranch Bow, The World Stone, Blood-Bound
    Book, Rod of Asclepius, Kinetic Cuirass, Freya''s Tears, Amanita Charm, Gem of
    Focus.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.52
    Death Metal:
      total: 0.51
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.77
      win: 0.51
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Shield of the Phoenix,
    Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Riptalon, Nimble
    Ring, Rod of Asclepius, Genji''s Guard, Chandra''s Grace, Pharaoh''s Curse, Oni
    Hunter''s Garb, Golden Blade, Runeforged Hammer, Phoenix Feather, Freya''s Tears,
    Breastplate of Valor, Spectral Armor, Death Metal, Blood-Bound Book, Erosion,
    Shogun''s Ofuda, Eye of the Storm, Damaru, Shield Splitter, Eye of Providence,
    Bancroft''s Talon, Lernaean Bow, Draconic Scale, Lifebinder, Leviathan''s Hide,
    Midgardian Mail, The Cosmic Horror, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.3
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.51
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
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
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Soul Gem, Nimble
    Ring, Riptalon, Tekko-Kagi, Silverbranch Bow, The Cosmic Horror, Spear of the
    Magus, Berserker''s Shield, Death Metal, Spear of Desolation, Damaru, Lernaean
    Bow, Genji''s Guard, Obsidian Shard, Golden Blade, Toxic Blade, Screeching Gargoyle,
    Runeforged Hammer, Pendulum Blade, Tyrfing, Breastplate of Valor, Doom Orb, Bragi''s
    Harp, Stone of Binding, The World Stone, Dominance, Kinetic Cuirass, Pharaoh''s
    Curse, Void Shield, Amanita Charm, Dreamer''s Idol, Avatar''s Parashu, Avenging
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.61
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.63
      win: 0.51
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.57
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.44
      win: 0.51
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.67
    Titan's Bane:
      total: 0.51
      efficiency: 0.45
      win: 0.56
      pick: 0.32
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - The Crusher
  flex_slots:
  - Golden Blade
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Nimble Ring, Rod of Tahuti, Riptalon, The Crusher, Gluttonous Grimoire,
    Golden Blade, Berserker''s Shield, Silverbranch Bow, Tyrfing, Soul Gem, Lernaean
    Bow, Genji''s Guard, Death Metal, Damaru, Toxic Blade, Tekko-Kagi, The Cosmic
    Horror, Pharaoh''s Curse, Runeforged Hammer, Breastplate of Valor, Spear of the
    Magus, Bragi''s Harp, Dominance, Bracer of The Abyss, Kinetic Cuirass, Amanita
    Charm, Transcendence, Eye of Providence, Shogun''s Ofuda, Spear of Desolation,
    Oni Hunter''s Garb, Blood-Bound Book, Freya''s Tears, Obsidian Shard, Eros'' Bow,
    Bancroft''s Talon, Qin''s Blade, Demon Blade.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.57
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.31
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.51
      efficiency: 0.53
      win: 0.51
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.51
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Spear of Desolation
  - The Crusher
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Genji''s
    Guard, Nimble Ring, The Crusher, Breastplate of Valor, Gluttonous Grimoire, Spear
    of Desolation, Chronos'' Pendant, Freya''s Tears, Berserker''s Shield, Shield
    of the Phoenix, Death Metal, The Cosmic Horror, Screeching Gargoyle, Gem of Focus,
    Chandra''s Grace, Spear of the Magus, Damaru, Totem of Death, Riptalon, Arondight,
    Lernaean Bow, Pendulum Blade, Silverbranch Bow, Golden Blade, Runeforged Hammer,
    Kinetic Cuirass, Amanita Charm, Bracer of The Abyss, Bragi''s Harp, Obsidian Shard,
    Pharaoh''s Curse, Tyrfing, Tekko-Kagi, Eye of Providence, Oni Hunter''s Garb,
    Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.51
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.59
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.5
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.34
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.51
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The Crusher
  - Rod of Tahuti
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, The Crusher, Nimble Ring, Gluttonous Grimoire,
    Death Metal, Berserker''s Shield, Damaru, Lernaean Bow, Soul Gem, Golden Blade,
    Tekko-Kagi, Riptalon, Tyrfing, Silverbranch Bow, Genji''s Guard, Bragi''s Harp,
    Runeforged Hammer, The Cosmic Horror, Spear of the Magus, Dominance, Breastplate
    of Valor, Pharaoh''s Curse, Spear of Desolation, Demon Blade, Bracer of The Abyss,
    Deathbringer, Kinetic Cuirass, Obsidian Shard, Amanita Charm, Transcendence, Avenging
    Blade, Toxic Blade, Pendulum Blade, Eye of Providence, Shield Splitter, Oni Hunter''s
    Garb.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.66
      win: 0.51
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.51
      pick: 0.45
      fit: 0.49
    Nimble Ring:
      total: 0.52
      efficiency: 0.68
      win: 0.51
      pick: 0.0
      fit: 0.31
    Death Metal:
      total: 0.5
      efficiency: 0.56
      win: 0.51
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.51
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.77
      win: 0.51
      pick: 0.0
      fit: 0.26
  starter: *id001
---
