---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.47
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.38
    win_rate: 0.59
    alternates:
    - name: Transcendence
      pick_rate: 0.31
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.1
      win_rate: 0.57
  - name: Transcendence
    pick_rate: 0.23
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.56
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.56
  - name: Hydra's Lament
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.56
  - name: Heartseeker
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.55
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.58
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.59
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.64
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.5
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.67
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.67
    - name: Skeggox
      pick_rate: 0.06
      win_rate: 0.47
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.4
    win_rate: 0.64
  - name: Bumba's Cudgel
    pick_rate: 0.27
    win_rate: 0.49
  - name: Archmage's Gem
    pick_rate: 0.1
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-08-21'
  god_win_rate: 0.5634674922600619
  god_matches_won: 546
  god_matches_played: 969
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Heartseeker
  flex_slots:
  - Tyrfing
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
    this god: Rod of Tahuti, Death Metal, The Crusher, Tyrfing, Berserker''s Shield,
    Golden Blade, Nimble Ring, Tekko-Kagi, Silverbranch Bow, Lernaean Bow, Riptalon,
    Gluttonous Grimoire, The Reaper, Soul Gem, Bragi''s Harp, Spear of the Magus,
    Runeforged Hammer, Toxic Blade, Spear of Desolation, Obsidian Shard, Dominance,
    Deathbringer, Damaru, Demon Blade, Genji''s Guard, Breastplate of Valor, Pharaoh''s
    Curse, Bracer of The Abyss, Amanita Charm, Shield Splitter, Musashi''s Dual Swords,
    Kinetic Cuirass, Doom Orb, Avatar''s Parashu, The Cosmic Horror, Avenging Blade,
    Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.72
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.64
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - Heartseeker
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation,
    The Crusher, Spear of the Magus, Berserker''s Shield, Obsidian Shard, Genji''s
    Guard, Bragi''s Harp, Breastplate of Valor, Tyrfing, Lernaean Bow, The Reaper,
    Doom Orb, Golden Blade, Tekko-Kagi, Runeforged Hammer, Ancient Signet, The World
    Stone, Helm of Radiance, Chronos'' Pendant, Silverbranch Bow, Dominance, Bracer
    of The Abyss, The Cosmic Horror, Riptalon, Ethereal Staff, Freya''s Tears, Wish-Granting
    Pearl, Rod of Asclepius, Amanita Charm, Dreamer''s Idol, Deathbringer, Kinetic
    Cuirass.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.28
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.52
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.28
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.54
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Soul Gem, Spear of Desolation, Gluttonous Grimoire, Death
    Metal, Nimble Ring, The Crusher, Spear of the Magus, Obsidian Shard, Berserker''s
    Shield, The Reaper, Silverbranch Bow, Tekko-Kagi, Genji''s Guard, Breastplate
    of Valor, Riptalon, Doom Orb, Tyrfing, The Cosmic Horror, Lernaean Bow, Bragi''s
    Harp, Golden Blade, The World Stone, Chronos'' Pendant, Freya''s Tears, Runeforged
    Hammer, Dreamer''s Idol, Toxic Blade, Helm of Radiance, Pendulum Blade, Bracer
    of The Abyss, Amanita Charm, Kinetic Cuirass, Ancient Signet, Ethereal Staff,
    Arondight, Shield of the Phoenix, Gem of Focus.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.16
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.56
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.16
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, The Reaper, Riptalon, Ethereal Staff, Rod of Asclepius,
    Gluttonous Grimoire, Golden Blade, Death Metal, Runeforged Hammer, Pharaoh''s
    Curse, Nimble Ring, Freya''s Tears, The Crusher, Genji''s Guard, Shifter''s Shield,
    Phoenix Feather, Breastplate of Valor, Shield Splitter, Shogun''s Ofuda, Yogi''s
    Necklace, Chandra''s Grace, Eye of the Storm, Spectral Armor, Mantle Of Discord,
    Stone of Binding, Tyrfing, Lernaean Bow, Blood-Bound Book, Erosion, Toxic Blade,
    Silverbranch Bow, Eye of Providence, Spear of the Magus, Lifebinder, Leviathan''s
    Hide, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.3
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.58
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
  - Heartseeker
  flex_slots:
  - Tekko-Kagi
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, The Crusher, Gluttonous Grimoire, Tekko-Kagi, Silverbranch
    Bow, Soul Gem, The Reaper, Riptalon, Spear of the Magus, Death Metal, Spear of
    Desolation, Obsidian Shard, Berserker''s Shield, Nimble Ring, Toxic Blade, Avenging
    Blade, Tyrfing, Golden Blade, Lernaean Bow, Doom Orb, Stone of Binding, The Cosmic
    Horror, The World Stone, Avatar''s Parashu, Screeching Gargoyle, Dreamer''s Idol,
    Runeforged Hammer, Pendulum Blade, Bragi''s Harp, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Dominance, Deathbringer, Damaru, Kinetic Cuirass, Void
    Shield, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.6
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.67
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.49
      win: 0.58
      pick: 0.0
      fit: 0.76
    The Crusher:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.57
      pick: 0.45
      fit: 0.77
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Tyrfing
  - Silverbranch Bow
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
    this god: Rod of Tahuti, Nimble Ring, Berserker''s Shield, Riptalon, Tyrfing,
    Silverbranch Bow, Golden Blade, Gluttonous Grimoire, Death Metal, Soul Gem, The
    Crusher, Lernaean Bow, The Reaper, Tekko-Kagi, Toxic Blade, Spear of the Magus,
    Bragi''s Harp, Genji''s Guard, Runeforged Hammer, Breastplate of Valor, Obsidian
    Shard, Spear of Desolation, Pharaoh''s Curse, Dominance, Amanita Charm, Bracer
    of The Abyss, Kinetic Cuirass, Qin''s Blade, Shogun''s Ofuda, Freya''s Tears,
    Deathbringer, Damaru, Helm of Radiance, Eye of Providence, Demon Blade, Shield
    Splitter, Doom Orb, The Cosmic Horror.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.3
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.66
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Spear of
    Desolation, Genji''s Guard, Breastplate of Valor, Nimble Ring, Freya''s Tears,
    Death Metal, Berserker''s Shield, Gluttonous Grimoire, Chronos'' Pendant, Shield
    of the Phoenix, The Crusher, Spear of the Magus, Screeching Gargoyle, Silverbranch
    Bow, Arondight, Gem of Focus, Obsidian Shard, Tyrfing, Riptalon, Lernaean Bow,
    Golden Blade, Pendulum Blade, Totem of Death, The Reaper, Tekko-Kagi, Amanita
    Charm, Runeforged Hammer, Bragi''s Harp, Kinetic Cuirass, Chandra''s Grace, Helm
    of Radiance, Bracer of The Abyss, Toxic Blade, Doom Orb, The Cosmic Horror, Pharaoh''s
    Curse, The World Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.1
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.59
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.1
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.24
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Soul Gem, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard,
    The Crusher, Berserker''s Shield, Bragi''s Harp, Genji''s Guard, Chronos'' Pendant,
    Breastplate of Valor, Doom Orb, The Reaper, The Cosmic Horror, Silverbranch Bow,
    Tyrfing, Helm of Radiance, Lernaean Bow, Tekko-Kagi, Bracer of The Abyss, Golden
    Blade, The World Stone, Riptalon, Dreamer''s Idol, Ancient Signet, Ethereal Staff,
    Runeforged Hammer, Rod of Asclepius, Freya''s Tears, Gem of Focus, Amanita Charm,
    Jade Scepter, Kinetic Cuirass, Totem of Death, Wish-Granting Pearl.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.46
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.54
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.41
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Nimble
    Ring, Gluttonous Grimoire, Soul Gem, The Crusher, Spear of the Magus, Spear of
    Desolation, Obsidian Shard, Berserker''s Shield, Bragi''s Harp, Tekko-Kagi, Tyrfing,
    The Reaper, Golden Blade, Lernaean Bow, Silverbranch Bow, Riptalon, Runeforged
    Hammer, Doom Orb, The Cosmic Horror, Bracer of The Abyss, The World Stone, Helm
    of Radiance, Dreamer''s Idol, Ancient Signet, Genji''s Guard, Breastplate of Valor,
    Ethereal Staff, Dominance, Deathbringer, Damaru, Rod of Asclepius, Toxic Blade,
    Chronos'' Pendant, Amanita Charm, Kinetic Cuirass, Shield Splitter.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.56
      pick: 0.22
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.31
      fit: 0.22
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.41
    Death Metal:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
    Underrated for this god: Rod of Tahuti, Death Metal, The Crusher, Tyrfing, Berserker''s
    Shield, Golden Blade, Nimble Ring, Tekko-Kagi, Silverbranch Bow, Lernaean Bow,
    Riptalon, Gluttonous Grimoire, Soul Gem, The Reaper, Bragi''s Harp, Spear of the
    Magus, Runeforged Hammer, Toxic Blade, Spear of Desolation, Obsidian Shard, Dominance,
    Deathbringer, Damaru, Demon Blade, Genji''s Guard, Breastplate of Valor, Pharaoh''s
    Curse, Bracer of The Abyss, Amanita Charm, Shield Splitter, Musashi''s Dual Swords,
    Kinetic Cuirass, Doom Orb, Avatar''s Parashu, The Cosmic Horror, Avenging Blade,
    Shogun''s Ofuda, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.59
      pick: 0.38
      fit: 0.49
    Tyrfing:
      total: 0.54
      efficiency: 0.48
      win: 0.58
      pick: 0.0
      fit: 0.72
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.27
  starter: *id001
---
